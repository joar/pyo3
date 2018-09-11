#![feature(specialization)]

#[macro_use]
extern crate pyo3;

use pyo3::prelude::*;


#[pyfunction]
fn acquire_the_gil() -> PyResult<String> {
    let gil = Python::acquire_gil();
    let py = gil.python();
    Ok("You can only see this on Python 3.7".into())
}

#[pymodinit]
fn vergil(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_function!(acquire_the_gil))?;
    Ok(())
}
