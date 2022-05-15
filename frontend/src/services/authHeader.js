import authService from "./authService";

export function authHeader() {
    const {getCurrentUser} = authService();
    const userToken = getCurrentUser();
    if (userToken && userToken.access) {
        return { Authorization: 'Bearer ' + userToken.access };
     } else {
        return {};
    }
}

export function refreshHeader () {
    const {getCurrentUser} = authService();
    const userToken = getCurrentUser();
    if (userToken && userToken.refresh) {
        return { Authorization: 'Bearer ' + userToken.refresh}
    } else {
        return {}
    }
}