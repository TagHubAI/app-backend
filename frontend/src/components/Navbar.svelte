<svelte:options tag="bar-component" />

<nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
        <a class="navbar-item" href="">
            <img src="images/logo.png" width="80" height="30" />
        </a>

        <a
            role="button"
            class="navbar-burger"
            aria-label="menu"
            aria-expanded="false"
            data-target="navbarBasicExample"
        >
            <span aria-hidden="true" />
            <span aria-hidden="true" />
            <span aria-hidden="true" />
        </a>
    </div>

    <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
            <a class="navbar-item"> Home </a>

            <a class="navbar-item"> Refinement </a>

            <div class="navbar-item has-dropdown is-hoverable">
                <a class="navbar-link"> Analytics </a>

                <div class="navbar-dropdown">
                    <a class="navbar-item"> [WA] Clusters Viewer</a>
                    <a class="navbar-item"> [WA] Product Word Frequency </a>
                    <a class="navbar-item"> [WA] Product wise KB Surfaced </a>
                    <a class="navbar-item"> [WA] Chatbot User Journey </a>
                    <a class="navbar-item"> [WD] Search Performance </a>
                    <hr class="navbar-divider" />
                    <a class="navbar-item"> Report an issue </a>
                </div>
            </div>
        </div>

        <div class="navbar-end">
            <div class="navbar-item">
                <div class="buttons">
                    <a class="button">
                        <strong>Sign up</strong>
                    </a>
                    <a class="button is-light"> Log in </a>
                </div>
            </div>
        </div>
    </div>
</nav>
