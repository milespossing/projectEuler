pub fn run() -> usize {
    primal::Primes::all().take_while(|&x| x < 2000000).sum()
}