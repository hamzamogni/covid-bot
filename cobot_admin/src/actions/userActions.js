import { GET_ERRORS, SET_CURRENT_USER, USER_LOADING } from "./types";
import axios from "axios";
import setAuthToken from "./../utils/setAuthToken";
import jwt_decode from "jwt-decode";

export const loginUser = data => dispatch => {
    dispatch({
        type: USER_LOADING
    });

    axios
        .post("api", data)
        .then(res => {
            // Get token
            const { token } = res.data;

            // Set to LocalStorage
            localStorage.setItem("jwtToken", token);

            // Set token to Auth header
            setAuthToken(token);

            const decoded = jwt_decode(token);
            // Set current user
            dispatch(setCurrentUser(decoded));
        })
        .catch(err =>
            dispatch({
                type: GET_ERRORS,
                payload: err.response.data
            })
        );
};

export const setCurrentUser = decoded => {
    return {
        type: SET_CURRENT_USER,
        payload: decoded
    };
};

export const registerUser = data => dispatch => {
    dispatch({
        type: USER_LOADING
    });

    axios
        .post("api", data)
        .then(res => {
            // Get token
            const { token } = res.data;

            // Set to LocalStorage
            localStorage.setItem("jwtToken", token);

            // Set token to Auth header
            setAuthToken(token);

            dispatch({
                type: SET_CURRENT_USER,
                payload: res.data
            });
        })
        .catch(err =>
            dispatch({
                type: GET_ERRORS,
                payload: err.response.data
            })
        );
};

export const logoutUser = () => dispatch => {
    // Remove token from localStorage
    localStorage.removeItem("jwtToken");
    // Remove auth header for future requests
    setAuthToken(false);
    // Set current user to {} which will set isAuthenticated to false
    dispatch(setCurrentUser({}));
};
