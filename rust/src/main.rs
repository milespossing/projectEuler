mod problems;
mod tools;

use std::env;
use clap::Parser;

#[derive(Parser)]
struct Args {
    #[clap(short, long)]
    problem: Option<u16>,
}

fn main() {
    let args = Args::parse();
    match args.problem {
        Some(problem) => {
            let result = problems::run(problem);
            if let Some(val) = result{
                println!("{}", val);
            } else {
                println!("-1");
            }
        } 
        None => {
            problems::run_all();
        }
    }
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