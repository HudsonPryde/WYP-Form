<template>
  <b-container>
    <b-form @submit.prevent="handleSubmit(form)" @reset="onReset" :v-if="show">
      <!-- email input -->
      <b-form-group
        id="email-lb"
        label="Email address:"
        label-for="email-input"
      >
        <b-form-input
          id="email-input"
          v-model="form.email"
          placeholder="Enter email"
          name="email"
          :validated="posted"
          :state="response['email']"
          class=""
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="name-lb"
        label="Your Name:"
        label-for="first-name-input"
      >
        <b-row>
          <!-- first name input -->
          <b-col>
            <b-form-input
              id="first-name-input"
              v-model="form.first_name"
              placeholder="Enter first name"
              name="first_name"
              :validated="posted"
              :state="response['first_name']"
              required
            ></b-form-input>
          </b-col>
          <!-- lsat name input -->
          <b-col>
            <b-form-input
              id="last-name-input"
              v-model="form.last_name"
              placeholder="Enter last name"
              name="last_name"
              :validated="posted"
              :state="response['last_name']"
              required
            ></b-form-input>
          </b-col>
        </b-row>
      </b-form-group>

      <!-- password input -->
      <b-form-group
        id="password-lb"
        label="Password: "
        label-for="password-input"
      >
        <b-form-input
          id="password-input"
          v-model="form.password"
          placeholder="Enter password"
          type="password"
          name="password"
          :validated="posted"
          required
        ></b-form-input>
      </b-form-group>

      <!-- phone input -->
      <b-form-group
        id="phone-lb"
        label="Phone Number: "
        label-for="phone-input"
      >
        <b-form-input
          id="phone-input"
          v-model="form.phone_num"
          placeholder="xxx-xxx-xxxx"
          type="tel"
          name="phone_num"
          :validated="posted"
          :state="response['phone_num']"
          required
        ></b-form-input>
      </b-form-group>

      <!-- address input -->
      <b-form-group id="address-lb" label="Address: " label-for="address-input">
        <b-form-input
          id="address-input"
          v-model="form.address"
          placeholder="Enter address"
          name="address"
          :validated="posted"
          :state="response['address']"
          required
        ></b-form-input>
      </b-form-group>

      <!-- City input -->
      <b-form-group id="city-lb" label="City: " label-for="city-input">
        <b-form-input
          id="city-input"
          v-model="form.city"
          placeholder="Enter city"
          name="city"
          :validated="posted"
          :state="response['city']"
          required
        ></b-form-input>
      </b-form-group>

      <!-- country input -->
      <b-form-group id="country-lb" label="Country: " label-for="country-input">
        <b-row>
          <b-col sm="2">
            <b-form-radio
              v-model="form.country"
              name="country-input"
              value="Canada"
              >Canada</b-form-radio
            >
          </b-col>
          <b-col sm="10">
            <b-form-radio
              v-model="form.country"
              name="country-input"
              value="USA"
              >USA</b-form-radio
            >
          </b-col>
        </b-row>
      </b-form-group>

      <!-- province input -->
      <div>
        <div class="mt-3" :v-text="'hello'">
          Province/State: {{ form.province }}
        </div>

        <b-form-select
          v-model="form.province"
          :options="options[form.country]"
          style="width: 25%;"
          :disabled="form.country == ''"
          name="province"
          required
        ></b-form-select>
      </div>
      <b-row>
      <b-col><b-button type="submit" variant="primary">Submit</b-button></b-col>
      <b-col><b-button type="reset" variant="danger">Reset</b-button></b-col>
      </b-row>
    </b-form>
    <br><br>
    <Toasts
      :show-progress="true"
      :rtl="true"
      :max-messages="5"
      :time-out="5000"
    ></Toasts>

  </b-container>
</template>

<script>
import axios from 'axios';
import provinces from '../data/provinces';

export default {
  name: 'Form',
  data() {
    return {
      form: {
        email: '',
        first_name: '',
        last_name: '',
        password: '',
        phone_num: '',
        address: '',
        city: '',
        province: '',
        country: '',
      },
      show: true,
      options: provinces,
      response: {},
      posted: false,
    };
  },
  methods: {
    handleSubmit(payload) {
      const path = 'http://localhost:5000/validation';
      axios.post(path, payload)
        .then((res) => {
          // const status = res.data
          // for
          console.log(res.data);
          this.response = res.data;
          this.posted = true;
          // check status
          if (this.checkStatus(this.response)) {
            // create a success message
            this.$toast.success('Success! Your info has been submitted.');
          } else {
            // create an error message
            this.$toast.error('Error! Some of your info is invalid.');
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.form.email = '';
      this.form.first_name = '';
      this.form.last_name = '';
      this.form.city = '';
      this.form.address = '';
      this.form.province = '';
      this.form.phone_num = '';
      this.form.country = '';
      this.form.password = '';
      this.posted = false;
      this.response = {};
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    checkStatus(data) {
      // check every input that needed to be validated for an invalid status
      const inputs = ['first_name', 'last_name', 'address', 'city', 'email', 'phone_num'];
      function getStatus(value) {
        return data[value];
      }
      return inputs.every(getStatus);
    },
  },
};
</script>

<style>

@media (min-width: 768px) {
  .container{
    width: 35% !important;
    padding: 1.25em;
    background-color: rgb(255, 255, 255);
    border-radius: 0.55em;
    box-shadow: 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }
  .btn-primary{
    margin-left: 70% !important;
  }
}

.form-control{
  margin-bottom: 10px;
}
.btn-primary{
  margin-left: 55%;
}

.toast-header > button {
  visibility: hidden;
}

</style>
