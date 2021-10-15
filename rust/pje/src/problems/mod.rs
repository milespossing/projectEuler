pub mod p002;
pub mod p003;
pub mod p010;

pub fn run_all() {
    println!("P2: {}", p002::run());
    println!("P3: {}", p003::run());
    println!("P10: {}", p010::run());
}