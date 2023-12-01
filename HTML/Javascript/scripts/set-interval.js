function runRepeatedly() {
    const date = new Date();
    console.log(date.toLocaleTimeString());
  }
  setInterval(runRepeatedly, 5000);