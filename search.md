---

<!-- HTML search field -->
<div id="search-container">
<input type="text" id="search-input" placeholder="Type your search here..." autofocus>
<ul id="results-container"></ul>
</div>

<!-- Grab search-script.js -->
<script src="/_assets/js/search-script.js" type="text/javascript"></script>

<!-- Configuration -->
<script>
SimpleJekyllSearch({
  searchInput: document.getElementById('search-input'),
  resultsContainer: document.getElementById('results-container'),
  json: '/search.json'
})
</script>