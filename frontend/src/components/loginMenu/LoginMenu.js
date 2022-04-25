import {useState} from "react";
import {Link, useNavigate} from "react-router-dom";

import './loginMenu.css'

const LoginMenu = () => {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [isSubmitted, setIsSubmitted] = useState(false);
    const [errorMessage, setErrorMessage] = useState({});
    const [passwordShown, setPasswordShown] = useState(false);
    const navigate = useNavigate()

    const handleChangeEmail = (event) => {
        setEmail(event.target.value)
    };

    const handleChangePassword = (event) => {
        setPassword(event.target.value)
    };

    const togglePassword = () => {
        setPasswordShown(!passwordShown)
    };

    const onHandleSubmitted = (event) => {
        event.preventDefault();
        if (!404) {
            setIsSubmitted(true)
        } else {
            alert('No such user');
        }
    };

    const renderErrorMessage = (name) =>
        name === errorMessage.name && (
            <div className='login-error'>{errorMessage.message}</div>
        );

    const renderForm = (
        <form onSubmit={onHandleSubmitted}>
            <div className='login-input'>
                <label className='login-label'>Email:</label>
                <input type='text' name='email' value={email} onChange={handleChangeEmail}/>
                {renderErrorMessage('email')}
            </div>
            <div className='login-input'>
                <label className='login-label'>Password:</label>
                <input type={passwordShown ? 'text' : 'password'} name='password' value={password} onChange={handleChangePassword}/>
                {renderErrorMessage('password')}
            </div>
            <div className='login-button'>
                <input type='submit' value='Log in'/>
            </div>
            <div className='login-button-wrapper'>
                <div className='login-show-password'>
                    <label>Show password</label>
                    <input type='checkbox' onChange={togglePassword}/>
                </div>
                <div className='login-question'>
                    <Link to='/register'>Don't have an account? Sign up!</Link>
                </div>
            </div>
        </form>
    )

    return (
        <div className='login-form'>
            <div className='login-title'>Sign in</div>
            {isSubmitted ? navigate('/') : renderForm}
        </div>
    )
}

export default LoginMenu;