<template>
  <div class="flex items-center min-h-screen p-4 bg-gray-100 lg:justify-center">
    <div
      class="flex flex-col overflow-hidden bg-white rounded-md shadow-lg max md:flex-row md:flex-1 lg:max-w-screen-md"
    >
      <div
        class="p-4 py-6 text-white bg-black md:w-80 md:flex-shrink-0 md:flex md:flex-col md:items-center md:justify-evenly"
      >
        <div class="my-3 text-4xl font-bold tracking-wider text-center">
          <a href="#">TagHub BI</a>
        </div>
        <p class="mt-6 font-normal text-center text-gray-300 md:mt-0">
          TagHub BI is a one-stop platform for crawling, processing, and visualize public data, either from social media, online services, or news!
        </p>
        <!-- <p class="flex flex-col items-center justify-center mt-10 text-center"> -->
        <!--   <span>Don't have an account?</span> -->
        <!--   <a href="#" class="underline">Get Started!</a> -->
        <!-- </p> -->
        <p class="mt-6 text-sm text-center text-gray-300">
          Read our <a href="#" class="underline">terms</a> and <a href="#" class="underline">conditions</a>
        </p>
      </div>
      <div class="p-5 bg-white md:flex-1">
        <h3 class="my-4 text-2xl font-semibold text-gray-700">
          Account Login
        </h3>
        <form action="#" class="flex flex-col space-y-5">
          <div class="flex flex-col space-y-1">
            <label for="email" class="text-sm font-semibold text-gray-500">Email address</label>
            <input
              id="email"
              type="email"
              autofocus
              class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:outline-none focus:ring-4 focus:ring-blue-200"
            >
          </div>
          <!-- No need password now  -->
          <!-- <div class="flex flex-col space-y-1"> -->
          <!--   <div class="flex items-center justify-between"> -->
          <!--     <label for="password" class="text-sm font-semibold text-gray-500">Password</label> -->
          <!--     <a href="#" class="text-sm text-blue-600 hover:underline focus:text-blue-800">Forgot Password?</a> -->
          <!--   </div> -->
          <!--   <input -->
          <!--     type="password" -->
          <!--     id="password" -->
          <!--     class="px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:outline-none focus:ring-4 focus:ring-blue-200" -->
          <!--   /> -->
          <!-- </div> -->
          <!-- <div class="flex items-center space-x-2"> -->
          <!--   <input -->
          <!--     type="checkbox" -->
          <!--     id="remember" -->
          <!--     class="w-4 h-4 transition duration-300 rounded focus:ring-2 focus:ring-offset-0 focus:outline-none focus:ring-blue-200" -->
          <!--   /> -->
          <!--   <label for="remember" class="text-sm font-semibold text-gray-500">Remember me</label> -->
          <!-- </div> -->
          <div>
            <button
              type="submit"
              class="w-full px-4 py-2 text-lg font-semibold text-white transition-colors duration-300 bg-black rounded-md shadow hover:bg-gray-600 focus:outline-none focus:ring-blue-200 focus:ring-4"
            >
              s  Sign me up!
            </button>
          </div>
          <div class="flex flex-col space-y-5">
            <span class="flex items-center justify-center space-x-2">
              <span class="h-px bg-gray-400 w-14" />
              <span class="font-normal text-gray-500">Don't have an account?</span>
              <span class="h-px bg-gray-400 w-14" />
            </span>
            <div class="flex flex-col space-y-4">
              <a
                href="#"
                class="flex items-center justify-center px-4 py-2 space-x-2 transition-colors duration-300 border border-gray-800 rounded-md group hover:bg-gray-800 focus:outline-none"
              >
                <span class="text-sm font-medium text-gray-800 group-hover:text-white">Send me magic link via email</span>
              </a>
              <!-- <a -->
              <!--   href="#" -->
              <!--   class="flex items-center justify-center px-4 py-2 space-x-2 transition-colors duration-300 border border-blue-500 rounded-md group hover:bg-blue-500 focus:outline-none" -->
              <!-- > -->
              <!--   <span> -->
              <!--     <svg class="text-blue-500 group-hover:text-white" width="20" height="20" fill="currentColor"> -->
              <!--       <path -->
              <!--         d="M6.29 18.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0020 3.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.073 4.073 0 01.8 7.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 010 16.407a11.616 11.616 0 006.29 1.84" -->
              <!--       ></path> -->
              <!--     </svg> -->
              <!--   </span> -->
              <!--   <span class="text-sm font-medium text-blue-500 group-hover:text-white">Twitter</span> -->
              <!-- </a> -->
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
