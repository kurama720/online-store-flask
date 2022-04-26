const isLogged = () => {
    const user = localStorage.getItem('user');
    return user !== null;
};

export default isLogged;