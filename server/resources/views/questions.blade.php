<!DOCTYPE html>
<html>

<head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/react/15.4.2/react.js" charset="utf-8"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/react/15.4.2/react-dom.js" charset="utf-8"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.21.1/babel.min.js" charset="utf-8"></script>
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <style>
        .root {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            padding: 0 10%;
        }

        .card {
            display: flex;
            padding: 10px 15px;
            justify-content: start;
            align-items: center;
            flex-direction: column;
            width: 100%;
            border-radius: 5px;
            border:1px solid #eeeeee;
            margin: 10px 0;

        }

        .content {
            display: flex;
            justify-content: start;
            width: 100%;
            align-items: center;


        }

        .expand {
            margin-left: auto;
        }

        .button {
            padding: 10px;
            background-color: #2e9c6a;
            cursor: pointer;
            color: white;
            margin: 30px 0;
        }

        .button:hover {
            box-shadow: 2px 2px 10px #aaaaaa;
        }
        .message {
            padding : 5px;
            background-color: #efefef;
            border-radius: 10px;
            margin:5px;
            max-width: 70%;
        }
        .reply{
            margin:5px ;
            margin-left: auto;
            padding : 5px;
            background-color: #2e9c6a;
            color: white;
            border-radius: 10px;
            max-width: 70%;
        }
    </style>


    <script type="text/babel">
        class Cobot extends React.Component {
            constructor(props) {
                super(props);
                this.state = {
                    messages: [],
                    loading: true,
                    page: null
                }

            }

            componentDidMount() {
                axios.get("http://localhost/api/messages")
                    .then(res => {
                        this.setState({
                            messages: res.data.data,
                            loading: false,
                            page: res.data.pagination.next_page
                        })
                        console.log(res)
                    })
            }

            loadMore = () => {
                let self = this
                axios.get(this.state.page)
                    .then(res => {
                        res.data.data.map(message => {
                            self.setState(prevState => {
                                return {
                                    ...prevState,
                                    messages: [...prevState.messages, message],
                                    page: res.data.pagination.next_page
                                }
                            })
                        })

                    })
            }

            render() {

                return <div className="root">
                    <h2>List of questions</h2>
                    {
                        this.state.loading ?

                            "Loading..." :
                            this.state.messages.map(message => (
                                <div className="card">
                                    <div className="content">
                                        <p className="message" >{message.message}</p>
                             
                                    </div>
                                    <div className="content">
                                    {
                                        message.replies.map(reply => (
                                            <p className="reply" >{reply.message}</p>

                                        ))
                                    }
                                    </div>
                                </div>
                            ))


                    }

                    <div onClick={this.loadMore} className="button">Load more</div>


                </div>;
            }
        }

        ReactDOM.render(React.createElement(Cobot), document.getElementById('chatbot'));
    </script>
</head>

<body>
    <div id="chatbot"></div>
</body>

</html>