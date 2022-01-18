use crate::tools;

static TARGET:usize = 600851475143;

pub fn run() -> usize{
    *tools::primes::get_prime_factors(TARGET).iter().max().unwrap()
}