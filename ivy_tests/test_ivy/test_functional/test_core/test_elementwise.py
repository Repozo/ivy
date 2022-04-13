"""
Collection of tests for elementwise functions
"""

# global
import pytest

# local
import ivy
import ivy_tests.test_ivy.helpers as helpers


# abs
@pytest.mark.parametrize(
    "dtype", ivy.all_dtype_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_abs(dtype, as_variable, with_out, native_array):
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([2, 3, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if not ivy.is_float_dtype(dtype):
            pytest.skip("only floating point variables are supported")
        if with_out:
            pytest.skip("variables do not support out argument")
        x = ivy.variable(x)
        out = ivy.variable(out)
    if native_array:
        x = x.data
        out = out.data
    if with_out:
        ret = ivy.abs(x, out=out)
    else:
        ret = ivy.abs(x)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# acosh
@pytest.mark.parametrize(
    "dtype", ivy.float_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_acosh(dtype, as_variable, with_out, native_array):
    if ivy.current_framework_str() == 'torch' and dtype == 'float16':
        pytest.skip("torch acosh doesnt allow float16")
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([2, 3, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if with_out:
            pytest.skip("variables do not support out argument")
        x = ivy.variable(x)
        out = ivy.variable(out)
    if native_array:
        x = x.data
        out = out.data
    if with_out:
        ret = ivy.acosh(x, out=out)
    else:
        ret = ivy.acosh(x)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# acos
@pytest.mark.parametrize(
    "dtype", ivy.float_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_acos(dtype, as_variable, with_out, native_array):
    if ivy.current_framework_str() == 'torch' and dtype == 'float16':
        pytest.skip("torch acos doesnt allow float16")
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([0.5, 0.8, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if with_out:
            pytest.skip("variables do not support out argument")
        x = ivy.variable(x)
        out = ivy.variable(out)
    if native_array:
        x = x.data
        out = out.data
    if with_out:
        ret = ivy.acos(x, out=out)
    else:
        ret = ivy.acos(x)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# add
@pytest.mark.parametrize(
    "dtype", ivy.all_dtype_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_add(dtype, as_variable, with_out, native_array):
    if ivy.current_framework_str() == 'numpy' and dtype == 'float16':
        pytest.skip("numpy array api doesnt support float16")
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([2, 3, 4], dtype=dtype)
    y = ivy.array([2, 3, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if not ivy.is_float_dtype(dtype):
            pytest.skip("only floating point variables are supported")
        if with_out:
            pytest.skip("variables do not support out argument")
        x = ivy.variable(x)
        y = ivy.variable(y)
        out = ivy.variable(out)
    if native_array:
        x = x.data
        y = y.data
        out = out.data
    if with_out:
        ret = ivy.add(x, y, out=out)
    else:
        ret = ivy.add(x, y)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# asin
@pytest.mark.parametrize(
    "dtype", ivy.float_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_asin(dtype, as_variable, with_out, native_array):
    if ivy.current_framework_str() == 'torch' and dtype == 'float16':
        pytest.skip("torch asin doesnt allow float16")
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([0.5, 0.8, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if with_out:
            pytest.skip("variables do not support out argument")
        x = ivy.variable(x)
        out = ivy.variable(out)
    if native_array:
        x = x.data
        out = out.data
    if with_out:
        ret = ivy.asin(x, out=out)
    else:
        ret = ivy.asin(x)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# asinh
@pytest.mark.parametrize(
    "dtype", ivy.float_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_asinh(dtype, as_variable, with_out, native_array):
    if ivy.current_framework_str() == 'torch' and dtype == 'float16':
        pytest.skip("torch asinh doesnt allow float16")
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([0.5, 0.8, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if with_out:
            pytest.skip("variables do not support out argument")
        x = ivy.variable(x)
        out = ivy.variable(out)
    if native_array:
        x = x.data
        out = out.data
    if with_out:
        ret = ivy.asinh(x, out=out)
    else:
        ret = ivy.asinh(x)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# atan
@pytest.mark.parametrize(
    "dtype", ivy.float_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_atan(dtype, as_variable, with_out, native_array):
    if ivy.current_framework_str() == 'torch' and dtype == 'float16':
        pytest.skip("torch atan doesnt allow float16")
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([0.5, 0.8, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if with_out:
            pytest.skip("variables do not support out argument")
        x = ivy.variable(x)
        out = ivy.variable(out)
    if native_array:
        x = x.data
        out = out.data
    if with_out:
        ret = ivy.atan(x, out=out)
    else:
        ret = ivy.atan(x)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# atan2
@pytest.mark.parametrize(
    "dtype", ivy.float_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_atan2(dtype, as_variable, with_out, native_array):
    if ivy.current_framework_str() == 'torch' and dtype in ['float16', 'bfloat16']:
        pytest.skip("torch atan2 doesnt allow float16 or bfloat16")
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x1 = ivy.array([2, 3, 4], dtype=dtype)
    x2 = ivy.array([2, 3, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if with_out:
            pytest.skip("variables do not support out argument")
        x1 = ivy.variable(x1)
        x2 = ivy.variable(x2)
        out = ivy.variable(out)
    if native_array:
        x1 = x1.data
        x2 = x2.data
        out = out.data
    if with_out:
        ret = ivy.atan2(x1, x2, out=out)
    else:
        ret = ivy.atan2(x1, x2)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# atanh
@pytest.mark.parametrize(
    "dtype", ivy.float_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_atanh(dtype, as_variable, with_out, native_array):
    if ivy.current_framework_str() == 'torch' and dtype == 'float16':
        pytest.skip("torch atanh doesnt allow float16")
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([0.5, 0.8, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if with_out:
            pytest.skip("variables do not support out argument")
        x = ivy.variable(x)
        out = ivy.variable(out)
    if native_array:
        x = x.data
        out = out.data
    if with_out:
        ret = ivy.atanh(x, out=out)
    else:
        ret = ivy.atanh(x)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# bitwise_and
@pytest.mark.parametrize(
    "dtype", ivy.int_strs + ['bool'])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_bitwise_and(dtype, with_out, native_array):
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x1 = ivy.array([0, 1, 1], dtype=dtype)
    x2 = ivy.array([0, 1, 1], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if native_array:
        x1 = x1.data
        x2 = x2.data
        out = out.data
    if with_out:
        ret = ivy.bitwise_and(x1, x2, out=out)
    else:
        ret = ivy.bitwise_and(x1, x2)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# bitwise_left_shift
@pytest.mark.parametrize(
    "dtype", ivy.int_strs)
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_bitwise_left_shift(dtype, with_out, native_array):
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x1 = ivy.array([0, 1, 1], dtype=dtype)
    x2 = ivy.array([0, 1, 1], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if native_array:
        x1 = x1.data
        x2 = x2.data
        out = out.data
    if with_out:
        ret = ivy.bitwise_left_shift(x1, x2, out=out)
    else:
        ret = ivy.bitwise_left_shift(x1, x2)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# bitwise_invert
@pytest.mark.parametrize(
    "dtype", ivy.int_strs + ['bool'])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_bitwise_invert(dtype, with_out, native_array):
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([0, 1, 1], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if native_array:
        x = x.data
        out = out.data
    if with_out:
        ret = ivy.bitwise_invert(x, out=out)
    else:
        ret = ivy.bitwise_invert(x)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# bitwise_or
@pytest.mark.parametrize(
    "dtype", ivy.int_strs + ['bool'])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_bitwise_or(dtype, with_out, native_array):
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x1 = ivy.array([0, 1, 1], dtype=dtype)
    x2 = ivy.array([0, 1, 1], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if native_array:
        x1 = x1.data
        x2 = x2.data
        out = out.data
    if with_out:
        ret = ivy.bitwise_or(x1, x2, out=out)
    else:
        ret = ivy.bitwise_or(x1, x2)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# bitwise_right_shift
@pytest.mark.parametrize(
    "dtype", ivy.int_strs)
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_bitwise_right_shift(dtype, with_out, native_array):
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x1 = ivy.array([0, 1, 1], dtype=dtype)
    x2 = ivy.array([0, 1, 1], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if native_array:
        x1 = x1.data
        x2 = x2.data
        out = out.data
    if with_out:
        ret = ivy.bitwise_right_shift(x1, x2, out=out)
    else:
        ret = ivy.bitwise_right_shift(x1, x2)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# bitwise_xor
@pytest.mark.parametrize(
    "dtype", ivy.int_strs + ['bool'])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_bitwise_xor(dtype, with_out, native_array):
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x1 = ivy.array([0, 1, 1], dtype=dtype)
    x2 = ivy.array([0, 1, 1], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if native_array:
        x1 = x1.data
        x2 = x2.data
        out = out.data
    if with_out:
        ret = ivy.bitwise_xor(x1, x2, out=out)
    else:
        ret = ivy.bitwise_xor(x1, x2)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# ceil
@pytest.mark.parametrize(
    "dtype", ivy.all_dtype_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_ceil(dtype, as_variable, with_out, native_array):
    # docstring test
    helpers.assert_docstring_examples_run(ivy.ceil)
    # rest tests out argument
    if ivy.current_framework_str() == 'torch' and dtype == 'float16':
        pytest.skip("torch ceil doesnt allow float16")
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([2, 3, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if not ivy.is_float_dtype(dtype):
            pytest.skip("only floating point variables are supported")
        if with_out:
            pytest.skip("variables do not support out argument")
        x = ivy.variable(x)
        out = ivy.variable(out)
    if native_array:
        x = x.data
        out = out.data
    if with_out:
        ret = ivy.ceil(x, out=out)
    else:
        ret = ivy.ceil(x)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# cos
@pytest.mark.parametrize(
    "dtype", ivy.float_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_cos(dtype, as_variable, with_out, native_array):
    if ivy.current_framework_str() == 'torch' and dtype == 'float16':
        pytest.skip("torch cos doesnt allow float16")
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([0.5, 0.8, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if with_out:
            pytest.skip("variables do not support out argument")
        x = ivy.variable(x)
        out = ivy.variable(out)
    if native_array:
        x = x.data
        out = out.data
    if with_out:
        ret = ivy.cos(x, out=out)
    else:
        ret = ivy.cos(x)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# cosh
@pytest.mark.parametrize(
    "dtype", ivy.float_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_cosh(dtype, as_variable, with_out, native_array):
    if ivy.current_framework_str() == 'torch' and dtype == 'float16':
        pytest.skip("torch cosh doesnt allow float16")
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([0.5, 0.8, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if with_out:
            pytest.skip("variables do not support out argument")
        x = ivy.variable(x)
        out = ivy.variable(out)
    if native_array:
        x = x.data
        out = out.data
    if with_out:
        ret = ivy.cosh(x, out=out)
    else:
        ret = ivy.cosh(x)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# divide
@pytest.mark.parametrize(
    "dtype", ivy.all_dtype_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_divide(dtype, as_variable, with_out, native_array):
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x1 = ivy.array([2, 3, 4], dtype=dtype)
    x2 = ivy.array([2, 3, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype='float64')
    if as_variable:
        if not ivy.is_float_dtype(dtype):
            pytest.skip("only floating point variables are supported")
        if with_out:
            pytest.skip("variables do not support out argument")
        x1 = ivy.variable(x1)
        x2 = ivy.variable(x2)
        out = ivy.variable(out)
    if native_array:
        x1 = x1.data
        x2 = x2.data
        out = out.data
    if with_out:
        ret = ivy.divide(x1, x2, out=out)
    else:
        ret = ivy.divide(x1, x2)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# equal
@pytest.mark.parametrize(
    "dtype", list(ivy.all_dtype_strs) + ['bool'])
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_equal(dtype, as_variable, with_out, native_array):
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x1 = ivy.array([2, 3, 4], dtype=dtype)
    x2 = ivy.array([2, 3, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if not ivy.is_float_dtype(dtype):
            pytest.skip("only floating point variables are supported")
        if with_out:
            pytest.skip("variables do not support out argument")
        x1 = ivy.variable(x1)
        x2 = ivy.variable(x2)
        out = ivy.variable(out)
    if native_array:
        x1 = x1.data
        x2 = x2.data
        out = out.data
    if with_out:
        ret = ivy.equal(x1, x2, out=out)
    else:
        ret = ivy.equal(x1, x2)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# exp
@pytest.mark.parametrize(
    "dtype", ivy.float_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_exp(dtype, as_variable, with_out, native_array):
    if ivy.current_framework_str() == 'torch' and dtype == 'float16':
        pytest.skip("torch exp doesnt allow float16")
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([0.5, 0.8, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if with_out:
            pytest.skip("variables do not support out argument")
        x = ivy.variable(x)
        out = ivy.variable(out)
    if native_array:
        x = x.data
        out = out.data
    if with_out:
        ret = ivy.exp(x, out=out)
    else:
        ret = ivy.exp(x)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# expm1
@pytest.mark.parametrize(
    "dtype", ivy.float_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_expm1(dtype, as_variable, with_out, native_array):
    if ivy.current_framework_str() == 'torch' and dtype == 'float16':
        pytest.skip("torch expm1 doesnt allow float16")
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([0.5, 0.8, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if with_out:
            pytest.skip("variables do not support out argument")
        x = ivy.variable(x)
        out = ivy.variable(out)
    if native_array:
        x = x.data
        out = out.data
    if with_out:
        ret = ivy.expm1(x, out=out)
    else:
        ret = ivy.expm1(x)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# floor
@pytest.mark.parametrize(
    "dtype", ivy.all_dtype_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_floor(dtype, as_variable, with_out, native_array):
    if ivy.current_framework_str() in ['torch', 'numpy'] and dtype == 'float16':
        pytest.skip("torch and numpy array api dont allow float16")
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([2, 3, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if not ivy.is_float_dtype(dtype):
            pytest.skip("only floating point variables are supported")
        if with_out:
            pytest.skip("variables do not support out argument")
        x = ivy.variable(x)
        out = ivy.variable(out)
    if native_array:
        x = x.data
        out = out.data
    if with_out:
        ret = ivy.floor(x, out=out)
    else:
        ret = ivy.floor(x)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# floor_divide
@pytest.mark.parametrize(
    "dtype", ivy.all_dtype_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_floor_divide(dtype, as_variable, with_out, native_array):
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x1 = ivy.array([2, 3, 4], dtype=dtype)
    x2 = ivy.array([2, 3, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if not ivy.is_float_dtype(dtype):
            pytest.skip("only floating point variables are supported")
        if with_out:
            pytest.skip("variables do not support out argument")
        x1 = ivy.variable(x1)
        x2 = ivy.variable(x2)
        out = ivy.variable(out)
    if native_array:
        x1 = x1.data
        x2 = x2.data
        out = out.data
    if with_out:
        ret = ivy.floor_divide(x1, x2, out=out)
    else:
        ret = ivy.floor_divide(x1, x2)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# greater
@pytest.mark.parametrize(
    "dtype", ivy.all_dtype_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_greater(dtype, as_variable, with_out, native_array):
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x1 = ivy.array([2, 3, 4], dtype=dtype)
    x2 = ivy.array([2, 3, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if not ivy.is_float_dtype(dtype):
            pytest.skip("only floating point variables are supported")
        if with_out:
            pytest.skip("variables do not support out argument")
        x1 = ivy.variable(x1)
        x2 = ivy.variable(x2)
        out = ivy.variable(out)
    if native_array:
        x1 = x1.data
        x2 = x2.data
        out = out.data
    if with_out:
        ret = ivy.greater(x1, x2, out=out)
    else:
        ret = ivy.greater(x1, x2)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# greater_equal
@pytest.mark.parametrize(
    "dtype", ivy.all_dtype_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_greater_equal(dtype, as_variable, with_out, native_array):
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x1 = ivy.array([2, 3, 4], dtype=dtype)
    x2 = ivy.array([2, 3, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if not ivy.is_float_dtype(dtype):
            pytest.skip("only floating point variables are supported")
        if with_out:
            pytest.skip("variables do not support out argument")
        x1 = ivy.variable(x1)
        x2 = ivy.variable(x2)
        out = ivy.variable(out)
    if native_array:
        x1 = x1.data
        x2 = x2.data
        out = out.data
    if with_out:
        ret = ivy.greater_equal(x1, x2, out=out)
    else:
        ret = ivy.greater_equal(x1, x2)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# isfinite
@pytest.mark.parametrize(
    "dtype", ivy.all_dtype_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_isfinite(dtype, as_variable, with_out, native_array):
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([2, 3, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if not ivy.is_float_dtype(dtype):
            pytest.skip("only floating point variables are supported")
        if with_out:
            pytest.skip("variables do not support out argument")
        x = ivy.variable(x)
        out = ivy.variable(out)
    if native_array:
        x = x.data
        out = out.data
    if with_out:
        ret = ivy.isfinite(x, out=out)
    else:
        ret = ivy.isfinite(x)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)


# isinf
@pytest.mark.parametrize(
    "dtype", ivy.all_dtype_strs)
@pytest.mark.parametrize(
    "as_variable", [True, False])
@pytest.mark.parametrize(
    "with_out", [True, False])
@pytest.mark.parametrize(
    "native_array", [True, False])
def test_isinf(dtype, as_variable, with_out, native_array):
    if dtype in ivy.invalid_dtype_strs:
        pytest.skip("invalid dtype")
    x = ivy.array([2, 3, 4], dtype=dtype)
    out = ivy.array([2, 3, 4], dtype=dtype)
    if as_variable:
        if not ivy.is_float_dtype(dtype):
            pytest.skip("only floating point variables are supported")
        if with_out:
            pytest.skip("variables do not support out argument")
        x = ivy.variable(x)
        out = ivy.variable(out)
    if native_array:
        x = x.data
        out = out.data
    if with_out:
        ret = ivy.isinf(x, out=out)
    else:
        ret = ivy.isinf(x)
    if with_out:
        if not native_array:
            assert ret is out
        if ivy.current_framework_str() in ["tensorflow", "jax"]:
            # these frameworks do not support native inplace updates
            return
        assert ret.data is (out if native_array else out.data)