<svelte:options tag="maindashboard-component" />

<script>
  async function getResultAPI() {
    const res = await fetch("http://127.0.0.1:8000/visualization/word_cloud");
    const text = await res.text();

    if (res.ok) {
      return text;
    } else {
      throw new Error(text);
    }
  }
  let promise = getResultAPI();
</script>

<div class="section">
  <div class="columns">
    <div class="column is-half">
      <table class="table is-fullwidth">
        <thead>
          <tr>
            <th><abbr title="Id">Id</abbr></th>
            <th><abbr title="Text">Text</abbr></th>
            <th><abbr title="Category">Category</abbr></th>
            <th><abbr title="Sentiment">Sentiment</abbr></th>
          </tr>
        </thead>
        <tfoot>
          <tr>
            <th><abbr title="Id">Id</abbr></th>
            <th><abbr title="Text">Text</abbr></th>
            <th><abbr title="Category">Category</abbr></th>
            <th><abbr title="Sentiment">Sentiment</abbr></th>
          </tr>
        </tfoot>
        <tbody>
          <tr>
            <th>Example</th>
            <td> This is somewhat cool </td>
            <td>
              <button class="button is-green is-light">Electronic</button>
            </td>
            <td>
              <button class="button is-warning is-light">Neutral</button>
            </td>
          </tr>
          <tr>
            <th>Example</th>
            <td> This is not ok!! </td><td>
              <button class="button is-green is-light">Electronic</button>
            </td>
            <td>
              <button class="button is-danger is-light">Negative</button>
            </td>
            <td />
          </tr>
          <tr>
            <th>Example</th>
            <td> This is too bad!! </td><td>
              <button class="button is-green is-light">Electronic</button>
            </td>
            <td>
              <button class="button is-success is-light">Positive</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="column">
      <div class="columns is-multiline">
        <div class="column is-half">
          <div class="card">
            <header class="card-header">
              <p class="card-header-title">Samples by topic</p>
            </header>
            <div class="card-content">
              <div class="content">
                <!-- <progress id="loader" class="progress is-small is-primary" max="100">15%</progress> -->
                <!-- <span id="graph_1" x-data="hey" x-text="await getWaitedData(1)"></span> -->
                <div id="graph_1" />
              </div>
            </div>
          </div>
        </div>
        <div class="column is-half">
          <div class="card">
            <header class="card-header">
              <p class="card-header-title">Sentiment by topic</p>
            </header>
            <div class="card-content">
              <div class="content">
                <span x-data x-text="await getWaitedData(3)" />
              </div>
            </div>
          </div>
        </div>
        <div class="column is-half">
          <div class="card">
            <header class="card-header">
              <p class="card-header-title">Sentiment over time</p>
            </header>
            <div class="card-content">
              <div class="content">
                <!-- <span x-data x-text="await getWaitedData(5)"></span> -->
              </div>
            </div>
          </div>
        </div>
        <div class="column is-half">
          <div class="card">
            <header class="card-header">
              <p class="card-header-title">Keyword Cloud</p>
            </header>
            <div class="card-content">
              {#await promise}
                <p>...waiting</p>
              {:then number}
                <p>The number is {number}</p>
              {:catch error}
                <p style="color: red">{error.message}</p>
              {/await}
            </div>
          </div>
        </div>
      </div>
      <div class="column is-fullwidth">
        <div class="card">
          <header class="card-header">
            <p class="card-header-title">Samples by sentiment by week</p>
          </header>
          <div class="card-content">
            <div class="content">
              <!-- <span x-data x-text="await getWaitedData(3)"></span> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="section">
  <!-- Import data   -->
  <h2 class="title is-2">Import data</h2>
  <form action="" method="post">
    <textarea
      name="textarea"
      class="textarea"
      placeholder="10 lines of textarea"
      rows="10"
    />
    <br />
    <button class="button is-black" type="submit" value="Submit">Submit</button>
  </form>
</div>
