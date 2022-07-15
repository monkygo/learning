import React, { Component } from "react";

class Counter extends Component {
  /* constructor(props) {
    super(props);
    // this.handleIncrement = this.handleIncrement.bind(this);
  } */

  /* state = {
    value: this.props.counter.value,
    tags: ["tag1", "tag2", "tag3"],
  }; */

  componentDidUpdate(prevProps, prevState) {
    console.log("prevProps", prevProps);
    console.log("prevState", prevState);
    if (prevProps.counter.value !== this.props.counter.value) {
      // Ajax call and get new data from the server
    }
  }

  componentWillUnmount() {
    console.log("Counter - Unmount");
  }

  styles = {
    fontSize: 50,
    fontWeight: "bold",
  };

  renderTags() {
    /* if (this.state.tags.length === 0) return <p>There are no tags!</p>;

    return (
      <ul>
        {this.state.tags.map((tag) => (
          <li key={tag}>{tag}</li>
        ))}
      </ul>
    ); */
  }

  /*  handleIncrement = () => {
    // this.setState({ ...this.state, value: this.state.value + 1 });
    // console.log(this.state);
  }; */

  formatValue() {
    const { value } = this.props.counter;
    return value === 0 ? "Zero" : value;
  }

  render() {
    this.getBadgeClasses();
    // console.log("props", this.props);
    console.log("Counter - Rendered");
    return (
      <div>
        {/*this.state.tags.length === 0 && "Please create a new tag!"*/}
        {
          //this.renderTags()
        }
        {this.props.children}
        <span className={this.getBadgeClasses()}>{this.formatValue()}</span>
        <button
          onClick={() => this.props.onIncrement(this.props.counter)}
          className="btn btn-secondary btn-sm"
        >
          Increment
        </button>
        <button
          onClick={() => this.props.onDelete(this.props.counter.id)}
          className="btn btn-danger btn-sm m-2"
        >
          Delete
        </button>
      </div>
    );
  }

  getBadgeClasses() {
    let classes = "badge m-2 badge-";
    classes += this.props.counter.value === 0 ? "warning" : "primary";
    return classes;
  }
}

export default Counter;
