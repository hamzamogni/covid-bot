<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <link rel="stylesheet" href="css/chatbot.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/react/15.4.2/react.js" charset="utf-8"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/react/15.4.2/react-dom.js" charset="utf-8"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.21.1/babel.min.js" charset="utf-8"></script>
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <script src="js/chatbot.js"></script>
  <script type="text/babel">

    ReactDOM.render(React.createElement(Cobot, {
      logo: "images/cobot.png",
      api: "http://35.211.212.220:5005/webhooks/rest/webhook",
      color: "#9883E5",
      initialMessage: "I am a chatbot, ask me!",
      title: "Cobot"
    }), document.getElementById('chatbot'));
  </script>
</head>

<body>
  <div id="chatbot"></div>
</body>

</html>