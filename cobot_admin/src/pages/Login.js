import React, { Component } from "react";
import {
    Typography,
    Button,
    Grid,
    FormControl,
    FormHelperText,
    Input,
    InputLabel,
    Container,
    Card,
    CardContent,
    Snackbar,
    SnackbarContent
} from "@material-ui/core";

import { loginUser } from "../actions/userActions";
import PropTypes from "prop-types";
import { connect } from "react-redux";

class Login extends Component {
    constructor() {
        super();
        this.state = {
            email: "",
            password: ""
        };
        this.onChange = this.onChange.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
        this.setState = this.setState.bind(this);
    }

    componentDidMount() {
        if (localStorage.token) {
            this.props.history.push("/");
        }
    }

    componentWillReceiveProps(nextProps) {
        if (nextProps.user.isAuthenticated) {
            this.props.history.push("/quizzes");
        }
    }

    onChange = e => {
        this.setState({ [e.target.name]: e.target.value });
    };

    onSubmit = e => {
        e.preventDefault();
        this.setState({ loading: true });

        const data = {
            email: this.state.email,
            password: this.state.password
        };
        this.props.loginUser(data);
    };

    render() {
        const { errors } = this.props.user;
        const { loading } = this.props.user;

        return (
            <div>
                <Container small="true">
                    <Grid
                        container
                        direction="row"
                        justify="center"
                        alignItems="center"
                        spacing={5}
                        style={{ minHeight: "100vh" }}
                    >
                        <Grid item xs={4}>
                            <Card>
                                <CardContent>
                                    <form onSubmit={this.onSubmit}>
                                        <Typography
                                            variant="h5"
                                            style={{
                                                color: "#4993D1"
                                            }}
                                        >
                                            Sign In
                                        </Typography>

                                        <FormControl
                                            error={!!errors.email}
                                            className="w-100 mb-4"
                                        >
                                            <InputLabel htmlFor="email">
                                                Email
                                            </InputLabel>
                                            <Input
                                                id="email"
                                                name="email"
                                                label="Email"
                                                value={this.state.email}
                                                onChange={this.onChange}
                                                required
                                                aria-describedby="email-error-text"
                                            />
                                            <FormHelperText id="email-error-text">
                                                {errors.email}
                                            </FormHelperText>
                                        </FormControl>
                                        <FormControl
                                            error={!!errors.password}
                                            className="w-100 mb-4"
                                        >
                                            <InputLabel htmlFor="password">
                                                Password
                                            </InputLabel>
                                            <Input
                                                id="password"
                                                name="password"
                                                label="Password"
                                                type="password"
                                                value={this.state.password}
                                                onChange={this.onChange}
                                                required
                                                aria-describedby="password-error-text"
                                            />
                                            <FormHelperText id="password-error-text">
                                                {errors.password}
                                            </FormHelperText>
                                        </FormControl>

                                        <Button
                                            type="submit"
                                            variant="contained"
                                            margin="normal"
                                            disabled={loading}
                                        >
                                            {loading ? "LOADING..." : "LOGIN"}
                                        </Button>
                                    </form>
                                </CardContent>
                            </Card>
                        </Grid>
                    </Grid>
                </Container>
            </div>
        );
    }
}

Login.propTypes = {
    user: PropTypes.object.isRequired,
    loginUser: PropTypes.func.isRequired
};

const mapStateToProps = state => ({
    user: state.user
});

export default connect(mapStateToProps, { loginUser })(Login);
