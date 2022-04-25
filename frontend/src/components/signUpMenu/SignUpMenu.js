import {useState} from "react";
import {Link, useNavigate} from "react-router-dom";

import './signUpMenu.css'

const SignUpMenu = () => {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [isSubmitted, setIsSubmitted] = useState(false);
    const [errorMessage, setErrorMessage] = useState({});
    const [passwordShown, setPasswordShown] = useState(false);
    const navigate = useNavigate()

    const handleChangeEmail = (event) => {
        setEmail(event.target.value)
    }

    const handleChangePassword = (event) => {
        setPassword(event.target.value)
    }

    const handleChangeConfirmPassword = (event) => {
        setConfirmPassword(event.target.value)
    }

    const togglePassword = () => {
        setPasswordShown(!passwordShown)
    };

    const onHandleSubmitted = (event) => {
        event.preventDefault();
        if (!/^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[A-Za-z]+$/.test(email) ) {
            setErrorMessage({name: 'email',message: 'Email is invalid'})
        } else if (password.length < 8) {
            setErrorMessage({name: 'password', message: "Password is too short"});
        } else if (password !== confirmPassword) {
            setErrorMessage({name: password, message: "Passwords don't match"})
        } else {
            setIsSubmitted(true)
        }
    }

    const renderErrorMessage = (name) =>
        name === errorMessage.name && (
            <div className='register-error'>{errorMessage.message}</div>
        );

    const renderForm = (
        <form onSubmit={onHandleSubmitted}>
            <div className='register-input'>
                <label className='register-label'>Email:</label>
                <input type='text' name='email' value={email} onChange={handleChangeEmail}/>
                {renderErrorMessage('email')}
            </div>
            <div className='register-input'>
                <label className='register-label'>Password:</label>
                <input type={passwordShown ? 'text' : 'password'} name='password' value={password} onChange={handleChangePassword}/>
                {renderErrorMessage('password')}
            </div>
            <div className='register-input'>
                <label className='register-label'>Confirm password:</label>
                <input type={passwordShown ? 'text' : 'password'} name='confirm-password' value={confirmPassword} onChange={handleChangeConfirmPassword}/>
                {renderErrorMessage('password')}
            </div>
            <div className='register-button'>
                <input type='submit' value='Sign Up'/>
            </div>
            <div className='register-button-wrapper'>
                <div className='register-show-password'>
                    <label>Show password</label>
                    <input type='checkbox' onChange={togglePassword}/>
                </div>
                <div className='register-question'>
                    <Link to='/login'>Already have an account? Log in!</Link>
                </div>
            </div>
        </form>
    )

    return (
        <div className='register-form'>
            <div className='register-title'>Sign Up</div>
            {isSubmitted ? navigate('/login') : renderForm}
        </div>
    )
}

export default SignUpMenu;