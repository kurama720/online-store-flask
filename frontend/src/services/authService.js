import useAPIService from "./APIService";

const AuthService = () => {
    const {loginUser, registerUser} = useAPIService();

    const login = (email, password) => {
        return loginUser(email, password).then(response => {
            if (response.data.access) {
                localStorage.setItem('user', JSON.stringify(response.data));
            }
            return response.data;
        });
    }

    const logout = () => {
        localStorage.removeItem('user');
    }

    const register = (email, password) => {
        return registerUser(email, password);
    }

    const getCurrentUser = () => {
        return JSON.parse(localStorage.getItem('user'));
    }

    return {login, logout, register, getCurrentUser}
}

export default AuthService;