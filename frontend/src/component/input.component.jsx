import React from "react";
//import axios from 'axios';
import './input.style.css';

class Info extends React.Component {
    render() {
        return (
            <div>
                <p style={{ fontSize: 18, color: "#F4D13EFF", fontFamily: 'Comic Sans MS' }}>
                    <h2>AMZN Stock</h2>
                    5.4697% of posts have a negative sentiment score
                    <br />
                    74.3243% of posts have a neutral sentiment score
                    <br />
                    20.2070% of posts have a positive sentiment score
                </p>

                <p style={{ fontSize: 15, color: "#d9e3f0", fontFamily: 'Arial' }}>
                    A sentiment score for a stock is a numerical value that represents the overall sentiment or attitude of investors towards a particular stock.
                    Our sentiment scores are generated based on the posts from <b><i>subreddit wallstreetbets on Reddit.</i> </b>Our sentiment score is categorized into negative, neutral, and positive sentiment ranging from zero to one, with zero being neutral.
                    A high positive sentiment score indicates that investors are generally bullish on the stock, while a high negative sentiment score indicates that investors are bearish on the stock.
                    We multiplied the sentiment score by a formula we created in order to balance out the weight of each post in terms of popularity.
                </p>
            </div>
        );
    }

}

class StockForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: '',
            score: 0,
            showInfo: false,

        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({ value: event.target.value });
    }

    handleSubmit(event) {
        // alert('A stock was submitted: ' + this.state.value);
        // stock_name = this.state.value
        // backend_func(stock_name)
        // fetchData()
        event.preventDefault();
        this.setState({ showInfo: true });
       
    }



    render() {
        return (
            <div className='input-container'>
                <form onSubmit={this.handleSubmit}>
                    <label>
                        <h1 style={{ fontSize: 40, color: "#F4D13EFF", fontFamily: 'Comic Sans MS' }}>
                            Welcome to Stocky
                        </h1>
                        <h1 style={{ fontSize: 30, color: "#F4D13EFF", fontFamily: 'Comic Sans MS' }}>
                            Which stock are you interested in?
                        </h1>
                        <input type="text" value={this.state.value} onChange={this.handleChange} />
                    </label>
                    <input type="submit" value="Submit" />
                </form>
                {this.state.showInfo ? <Info /> : null}
                <div>

                </div>
            </div>
        );
    }
}

export default StockForm;