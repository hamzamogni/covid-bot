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
    "use strict";function _instanceof(e,t){return null!=t&&"undefined"!=typeof Symbol&&t[Symbol.hasInstance]?!!t[Symbol.hasInstance](e):e instanceof t}function _typeof(e){return(_typeof="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(e)}function _toConsumableArray(e){return _arrayWithoutHoles(e)||_iterableToArray(e)||_unsupportedIterableToArray(e)||_nonIterableSpread()}function _nonIterableSpread(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}function _unsupportedIterableToArray(e,t){if(e){if("string"==typeof e)return _arrayLikeToArray(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(r):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?_arrayLikeToArray(e,t):void 0}}function _iterableToArray(e){if("undefined"!=typeof Symbol&&Symbol.iterator in Object(e))return Array.from(e)}function _arrayWithoutHoles(e){if(Array.isArray(e))return _arrayLikeToArray(e)}function _arrayLikeToArray(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}function _classCallCheck(e,t){if(!_instanceof(e,t))throw new TypeError("Cannot call a class as a function")}function _defineProperties(e,t){for(var r=0;r<t.length;r++){var n=t[r];n.enumerable=n.enumerable||!1,n.configurable=!0,"value"in n&&(n.writable=!0),Object.defineProperty(e,n.key,n)}}function _createClass(e,t,r){return t&&_defineProperties(e.prototype,t),r&&_defineProperties(e,r),e}function _inherits(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function");e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,writable:!0,configurable:!0}}),t&&_setPrototypeOf(e,t)}function _setPrototypeOf(e,t){return(_setPrototypeOf=Object.setPrototypeOf||function(e,t){return e.__proto__=t,e})(e,t)}function _createSuper(e){return function(){var t,r=_getPrototypeOf(e);if(_isNativeReflectConstruct()){var n=_getPrototypeOf(this).constructor;t=Reflect.construct(r,arguments,n)}else t=r.apply(this,arguments);return _possibleConstructorReturn(this,t)}}function _possibleConstructorReturn(e,t){return!t||"object"!==_typeof(t)&&"function"!=typeof t?_assertThisInitialized(e):t}function _assertThisInitialized(e){if(void 0===e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return e}function _isNativeReflectConstruct(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],function(){})),!0}catch(e){return!1}}function _getPrototypeOf(e){return(_getPrototypeOf=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)})(e)}function _defineProperty(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var Cobot=function(e){_inherits(r,React.Component);var t=_createSuper(r);function r(e){var n;return _classCallCheck(this,r),_defineProperty(_assertThisInitialized(n=t.call(this,e)),"onSubmit",function(e){var t=_assertThisInitialized(n);if(""!=n.state.message){e.preventDefault();var r={message:n.state.message,user:!0};n.setState(function(e){return{...e,messages:[].concat(_toConsumableArray(e.messages),[r]),message:"",loading:!0}}),n.props.api||console.error("Api not found! you must specify the api URL."),axios.post(n.props.api,{message:n.state.message}).then(function(e){console.log(e),t.setState(function(t){return{...t,messages:[].concat(_toConsumableArray(t.messages),[{message:e.data.message}]),loading:!1}})})}}),_defineProperty(_assertThisInitialized(n),"onChange",function(e){n.setState(_defineProperty({},e.target.name,e.target.value))}),_defineProperty(_assertThisInitialized(n),"onOpen",function(){n.setState(function(e){return{...e,open:!e.open}})}),n.state={messages:[{message:e.initialMessage?e.initialMessage:"I am bot, ask me anything!"}],message:"",open:!1,loading:!1},n}return _createClass(r,[{key:"componentDidUpdate",value:function(){var e=document.querySelector("#chats");e.scrollTop=e.scrollHeight}},{key:"render",value:function(){var e=this;return React.createElement("div",null,React.createElement("div",{className:"root",style:this.state.open?{display:""}:{display:"none"}},React.createElement("div",{className:"header",style:this.props.color?{backgroundColor:this.props.color}:null},React.createElement("h3",{className:"title"},this.props.title?this.props.title:"Chatbot"),React.createElement("i",{className:"material-icons closeicon",onClick:this.onOpen},"close")),React.createElement("div",{className:"chats",id:"chats"},this.state.messages.map(function(t){return t.user?React.createElement("div",{className:"messagerootuser",style:e.props.color?{backgroundColor:e.props.color}:null},t.message):React.createElement("div",{className:"messageroot"},t.message)}),this.state.loading?React.createElement("div",{className:"typing-indicator"},React.createElement("span",null),React.createElement("span",null),React.createElement("span",null)):null),React.createElement("form",{onSubmit:this.onSubmit},React.createElement("div",{className:"inputgrid"},React.createElement("input",{required:!0,className:"input",autoComplete:"off",onChange:this.onChange,name:"message",value:this.state.message,placeholder:"Write your message here..."}),React.createElement("i",{className:"material-icons sendicon",onClick:this.onSubmit,type:"submit"},"send")))),React.createElement("div",{onClick:this.onOpen,style:this.state.open?{display:"none"}:{display:""}},React.createElement("img",{src:this.props.logo?this.props.logo:"https://placeimg.com/50/50/tech",className:"cobotlogo"})))}}]),r}();
    
    ReactDOM.render(React.createElement(Cobot, {
      logo: "images/cobot.png",
      api: "http://35.211.212.220/api/predict",
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