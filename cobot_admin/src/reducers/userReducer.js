import { GET_ERRORS, SET_CURRENT_USER, USER_LOADING } from "../actions/types";
import isEmpty from "is-empty";

const initialState = {
    isAuthenticated: false,
    loading: false,
    user: {},
    errors: {}
};

export default function(state = initialState, action) {
    switch (action.type) {
        case GET_ERRORS:
            return {
                ...state,
                errors: action.payload,
                loading: false
            };
        case USER_LOADING:
            return {
                ...state,
                loading: true
            };
        case SET_CURRENT_USER:
            return {
                ...state,
                isAuthenticated: !isEmpty(action.payload),
                user: action.payload,
                loading: false,
                errors: {}
            };

        default:
            return state;
    }
}
