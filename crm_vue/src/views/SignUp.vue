<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Sign up</h1>

        <form action="">
          <div class="field">
            <label for="email">Email</label>
            <div class="control">
              <input type="email" name="email" id="email" class="input" />
            </div>
          </div>

          <div class="field">
            <label for="password1">Password</label>
            <div class="control">
              <input
                type="password"
                name="password1"
                id="password1"
                class="input"
              />
            </div>
          </div>

          <div class="field">
            <label for="password2">Repeat password</label>
            <div class="control">
              <input
                type="password"
                name="password2"
                id="password2"
                class="input"
              />
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-success">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUp',
}
</script>