// Exhaustive integer-only exclusion below 10^10.
// No class-number table, primality oracle, or floating-point arithmetic is used.
// Compile: g++ -O2 -std=c++17 verify_sieve.cpp -o verify_sieve
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>

using u64 = std::uint64_t;

int main() {
    constexpr u64 limit = 10000000000ULL; // exclusive
    constexpr int max_prime = 109;
    constexpr u64 large_begin = 4 * max_prime + 1;
    const auto start = std::chrono::steady_clock::now();
    std::vector<int> primes;
    for (int n = 3; n <= max_prime; n += 2) {
        bool prime = true;
        for (int d = 2; d * d <= n; ++d)
            if (n % d == 0) { prime = false; break; }
        if (prime) primes.push_back(n);
    }
    std::vector<std::vector<bool>> inert;
    for (int p : primes) {
        std::vector<bool> squares(p, false), ok(p, false);
        for (int a = 0; a < p; ++a) squares[a * a % p] = true;
        for (int r = 0; r < p; ++r) ok[r] = !squares[(p - r) % p];
        inert.push_back(ok);
    }
    // Build a CRT wheel: q = 3 (mod 8), and (-q/p)=-1 for p<=17.
    u64 modulus = 8;
    std::vector<u64> residues{3};
    std::size_t wheel_primes = 0;
    while (wheel_primes < primes.size() && primes[wheel_primes] <= 17) {
        int p = primes[wheel_primes];
        std::vector<u64> next;
        for (u64 r : residues)
            for (int k = 0; k < p; ++k) {
                u64 v = r + modulus * k;
                if (inert[wheel_primes][v % p]) next.push_back(v);
            }
        modulus *= p;
        residues = std::move(next);
        ++wheel_primes;
    }
    std::sort(residues.begin(), residues.end());
    std::vector<u64> rejected(primes.size(), 0), survivors;
    u64 checked = 0;
    for (u64 base = 0; base < limit; base += modulus) {
        for (u64 r : residues) {
            u64 q = base + r;
            if (q < large_begin || q >= limit) continue;
            ++checked;
            bool survives = true;
            for (std::size_t i = wheel_primes; i < primes.size(); ++i) {
                if (!inert[i][q % primes[i]]) {
                    ++rejected[i];
                    survives = false;
                    break;
                }
            }
            if (survives) survivors.push_back(q);
        }
    }
    std::vector<u64> small;
    for (u64 q = 11; q < large_begin; q += 8) {
        bool survives = true;
        for (std::size_t i = 0; i < primes.size() && 4ULL * primes[i] < q; ++i)
            if (!inert[i][q % primes[i]]) { survives = false; break; }
        if (survives) small.push_back(q);
    }
    std::cout << "limit_exclusive " << limit << "\n";
    std::cout << "large_begin " << large_begin << "\n";
    std::cout << "wheel_modulus " << modulus << "\n";
    std::cout << "wheel_residues " << residues.size() << "\n";
    std::cout << "large_candidates_checked " << checked << "\n";
    for (std::size_t i = wheel_primes; i < primes.size(); ++i)
        if (rejected[i]) std::cout << "first_rejecting_prime " << primes[i] << " count " << rejected[i] << "\n";
    std::cout << "large_survivors " << survivors.size() << "\n";
    for (u64 q : survivors) std::cout << "large_survivor " << q << "\n";
    std::cout << "small_survivors";
    for (u64 q : small) std::cout << " " << q;
    std::cout << "\n";
    std::cout << "elapsed_seconds "
              << std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count()
              << "\n";
    if (!survivors.empty() || small != std::vector<u64>{11,19,43,67,163})
        throw std::runtime_error("Unexpected survivors: inspect the output.");
}
