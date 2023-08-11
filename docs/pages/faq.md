# Frequently Asked Questions

<details>
<summary><h2>Does Sweep write tests?</h2></summary>

Yep! The easiest way to have Sweep write tests is by modifying the `description` parameter in your `sweep.yaml`. You can add something like:
“In <your repository>, the tests are written in <your format>. If you modify business logic, modify the tests as well using this format.” You can add anything you’d like to the description parameter, including formatting rules (like PEP8), code style, etc!

</details>

<details>
<summary><h2>Can we trust the code written by Sweep?</h2></summary>

You should always review the PR. However, we also perform testing to make sure the PR works using your existing GitHub actions. 
To get the best performance, add GitHub actions that lint, test, and validate your code.

</details>

<details>
<summary><h2>Can I have Sweep work off of another branch besides main?</h2></summary>

Yes! In the `sweep.yaml`, you can set the `branch` parameter to something besides your default branch, and Sweep will use that as a reference.

</details>

<details>
<summary><h2>Can I give documentation to Sweep?</h2></summary>

Yes! In the `sweep.yaml`, you can specify docs. Be sure to pick the prefix of the site, which will allow us to only fetch the docs you need.
Check out the example here: https://github.com/sweepai/sweep/blob/main/sweep.yaml.

</details>

<details>
<summary><h2>Can I comment on Sweep’s PRs?</h2></summary>

Yep! You have three options depending on the degree of the change:

1. You can comment on the issue, and Sweep will rewrite the entire pull request. This will use one of your GPT4 credits.
2. You can comment on the pull request (not a file) and Sweep can make substantial changes to the pull request. Sweep will search the codebase, and is able to modify and create files.
3. You can comment on the file directly, and Sweep will only modify that file. Use this for small single file changes.

</details>

<details>
<summary><h2>Why are you open source?</h2></summary>

We’re open source so that our users can see exactly how their data is processed, as well as learn from how Sweep works! We’re really excited about building a community of Sweep users(like you!).

</details>

<details>
<summary><h2>What’s the difference from CoPilot?</h2></summary>

Copilot lives in your IDE and writes small chunks of code at a time. This takes ~3-5 seconds, and you need to watch it the entire time. Sweep runs completely asynchronously, and handles the task end to end. This might take 10-15 minutes, but you’re able to walk away and come back to a finished pull request. Copilot also doesn’t have access to the latest documentation.

</details>

<details>
<summary><h2>What’s the difference from ChatGPT?</h2></summary>

ChatGPT can’t write the actual PR, and you’d have to paste the generated code into your codebase and create a PR yourself. ChatGPT doesn’t have access to your codebase and the latest documentation, so it’s limited with large software projects.

</details>

<details>
<summary><h2>What’s the difference from AutoGPT?</h2></summary>

AutoGPT(and similar tools) doesn’t work, and Sweep works. We don’t allow the language model to perform open domain tool execution (which doesn’t work well). We perform a fixed flow of search → plan → write code → validate code, repeating the last two steps. This lets us reliably generate PRs corresponding to the user description.

</details>

<details>
<summary><h2>Do you store our code?</h2></summary>

We access your GitHub repository at runtime. At the end of execution, your code is deleted from the server. To perform search over your codebase, we use the hashed contents along with the embeddings. This allows us to avoid storing any code as plaintext. Read more about it here: [https://docs.sweep.dev/blogs/search-infra](https://docs.sweep.dev/blogs/search-infra).

</details>

<details>
<summary><h2>Do you have example Sweep PRs?</h2></summary>

Yes! Check out [https://docs.sweep.dev/examples](https://docs.sweep.dev/examples).

</details>

<details>
<summary><h2>Can I host Sweep myself?</h2></summary>

Not at the moment, we want to work closely with all of our users and respond to their feedback. Self hosting doesn’t allow us to do this at the moment. Please reach out at team@sweep.dev if you have more questions.

</details>