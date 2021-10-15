mod problems;
mod tools;

fn main() {
    problems::run_all();
}

#[cfg(test)]
mod tests {
    #[test]
    fn p2() {
        let output = crate::problems::p2::run();
        assert_eq!(output, 4613732);
    }

    #[test]
    fn p3() {
        let output = crate::problems::p3::run();
        assert_eq!(output, 6857);
    }
}