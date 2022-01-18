pub mod p002;
pub mod p003;
pub mod p010;

pub fn run_all() {
    println!("P2: {}", p002::run());
    println!("P3: {}", p003::run());
    println!("P10: {}", p010::run());
}

pub fn run(n:u16) -> Option<String> {
    match n {
        2 => Some(p002::run().to_string()),
        3 => Some(p003::run().to_string()),
        10 => Some(p010::run().to_string()),
        _ => None,
    }
}