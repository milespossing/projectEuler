#[allow(dead_code)]
pub fn get_prime_factors(mut x:usize) -> Vec<usize> {
    let mut output:Vec<usize> = Vec::new();
    let mut primes = primal::Primes::all();
    while x > 1 {
        let current = primes.next().unwrap();
        while x % current == 0 { 
            x /= current;
            output.push(current);
        }
    }
    output
}

#[cfg(test)]
mod tests {
    #[test]
    fn gets_prime_factors() {
        let output = super::get_prime_factors(20);
        assert_eq!(output,vec![2, 2, 5]);
    }
}