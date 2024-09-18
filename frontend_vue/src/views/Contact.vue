<template>
    <VueFileManager title="contact-form" :hasSeparate="true">
        <template v-slot:sidebar>
            <VueSidebarDropdown title="contacts">
                <VueContactLinks />
            </VueSidebarDropdown>
        </template>
        <template v-slot:leftContent>
            <div class="contact-form-container">
                <form action="" class="contact-form" v-on:submit.prevent="sentMessage" v-if="status == 'nothing' || status == 'processing'">
                    <p>
                        <label for="id_name">_name:</label> <input v-model="name" type="text" name="name" maxlength="60"
                            required="required" id="id_name">
                    </p>
                    <p>
                        <label for="id_email">_email:</label> <input v-model="email" type="email" name="email"
                            maxlength="60" required="required" id="id_email">
                    </p>
                    <p>
                        <label for="id_content">_message:</label> <textarea v-model="message" name="content" cols="40"
                            rows="10" required="required" id="id_content"></textarea>
                    </p>
                    <VueButton id="contact-submit" type="submit" :disabled="status == 'processing'">
                        <span v-if="status == 'nothing'">submit-message</span>
                        <span v-else-if="status == 'processing'">sending...</span>
                        <span v-else>Error</span>
                    </VueButton>
                </form>
                <div id="contact-success" v-else-if="status == 'completed'">
                    <h2>Thank you! 🤘</h2>
                    <div class="text">Your message has been accepted. You will recieve answer really soon!</div>
                </div>
                <div id="contact-success" v-else>
                    <h2>Error 😔</h2>
                    <div class="text">An unexpected error has occurred. Try again.</div> <button
                        id="contact-new" type="button" class="btn" @click="replyMessage">send-new-message</button>
                </div>
            </div>
        </template>
        <template v-slot:rightContent>
            <pre><code class="language-js hljs language-javascript" data-highlighted="yes"><span class="hljs-keyword">const</span> button = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">querySelector</span>(<span class="hljs-string">'#sendBtn'</span>);

<span class="hljs-keyword">const</span> message = {
    <span class="hljs-attr">name</span>: <span class="hljs-string">"{{ name }}"</span>,
    <span class="hljs-attr">email</span>: <span class="hljs-string">"{{ email }}"</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">"{{ message }}"</span>,
    <span class="hljs-attr">date</span>: <span class="hljs-string">"{{ getCurrentDate }}"</span>
    
}
            
button.<span class="hljs-title function_">addEventListener</span>(<span class="hljs-string">'click'</span>, <span class="hljs-function">() =&gt; {</span>
    form.<span class="hljs-title function_">send</span>(message));
}
</code>
</pre>

        </template>

    </VueFileManager>
</template>

<script>
import VueFileManager from '@/components/UI/VueFileManager.vue';
import VueContactLinks from '@/components/UI/VueContactLinks.vue';
import axios from 'axios';
import VueButton from '@/components/UI/VueButton.vue';

export default {
    name: 'ContactPage',
    components: { VueFileManager, VueContactLinks, VueButton },
    data() {
        return {
            name: '',
            email: '',
            message: '',
            status: 'nothing', // nothing, processing, completed, error
        }
    },
    computed: {
        getCurrentDate() {
            // Получаем текущую дату
            let currentDate = new Date();

            // Получаем компоненты даты (день, месяц, год)
            let day = currentDate.getDate();
            let month = currentDate.getMonth() + 1; // Месяцы в JavaScript нумеруются с 0
            let year = currentDate.getFullYear();

            // Форматируем компоненты даты в нужный формат (добавляем ведущие нули при необходимости)
            let formattedDate = (day < 10 ? '0' : '') + day + '.' + (month < 10 ? '0' : '') + month + '.' + year;

            return formattedDate;
        }
    },
    methods: {
        sentMessage() {
            this.status = 'processing';
            axios.post('/api/v1/feedback/send-message/', {
                name: this.name,
                email: this.email,
                message: this.message

            }).then((response) => {
                this.status = 'completed';

            }).catch((error) => {
                console.log(error);
                this.status = 'error';

            });
        },
        replyMessage() {
            this.status = "nothing";
            this.name = "";
            this.email = "";
            this.message = "";
        }
    }
}
</script>

<style scoped>
.contact-form-container {
    max-width: 375px;
    width: 100%;
    margin: 0 auto;
    margin-top: 60px;
}

.contact-form-container p {
    margin-bottom: 20px;
}

form label {
    display: block;
    font-size: 16px;
    margin-bottom: 10px;
}

.hljs-built_in {
    color: #5565E8;
}
#contact-success {
  text-align: center;
}
#contact-success h2 {
  font-size: 26px;
}
#contact-success .text {
  padding: 25px 0;
  line-height: 24px;
}
</style>