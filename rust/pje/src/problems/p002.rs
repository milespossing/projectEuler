struct Fibonacci(u64, u64);

impl Iterator for Fibonacci {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        let ret = self.0;
        self.0 = self.1;
        self.1 += ret;

        Some(ret)
    }
}

pub fn run() -> u64{
    return Fibonacci(0,1)
        .filter(|&x| x % 2 == 0)
        .take_while(|&x| x < 4000000)
        .sum();
}
