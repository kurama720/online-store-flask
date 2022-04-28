import authService from "./authService";

export default function authHeader() {
    const {getCurrentUser} = authService();
    const userToken = getCurrentUser();
    if (userToken && userToken.access) {
        return { Authorization: 'Bearer ' + userToken.access };
     } else {
        return {};
    }
}