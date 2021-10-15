mod problems;
mod tools;

fn main() {
    problems::run_all();
}

#[cfg(test)]
mod tests {
    #[test]
    fn p2() {
        let output = crate::problems::p002::run();
        assert_eq!(output, 4613732);
    }

    #[test]
    fn p3() {
        let output = crate::problems::p003::run();
        assert_eq!(output, 6857);
    }

    #[test]
    fn p010(){
        let output = crate::problems::p010::run();
        assert_eq!(output, 142913828922);
    }
}