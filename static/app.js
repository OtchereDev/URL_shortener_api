const form = document.querySelector('form')
const message = document.querySelector('.message')
const info_cont = document.querySelector('.info')
const middle_cont = document.querySelector('.middle')


// classes
class Output {
    constructor(data) {
        this.data=data
    }
    createHTML() {
        const html = document.createElement('section')
        html.classList.add('output')
        html.innerHTML = `<div class="outcome">
                <div class="links">
                    <div class="real_link">
                        ${this.data.original_link}
                    </div>
                    <hr>
                    <div class="gen_link">
                        ${this.data.shortened_link}
                    </div>
                </div>
                <div class="copy">
                    <button class="copy_btn">
                        Copy
                    </button>
                </div>
            </div>`
        return html
    }

    insertHTML() {
        const html = this.createHTML()
        middle_cont.insertBefore(html, info_cont)
    }
}

// functions
function copyToClipboard(div) {
    const range = document.createRange()
    range.selectNode(div)
    window.getSelection().removeAllRanges()
    window.getSelection().addRange(range)
    document.execCommand('copy')
    window.getSelection().removeAllRanges()
}

async function postToAPI(input) {
    let body_msg={
        original_link: `${input}`,
        shortened_link: ""
    }

    response = await fetch('api/', {
        body: JSON.stringify(body_msg),
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'post'
    });

   data =  await response.json()

    // console.log(data)
    return data
}



// event listeners
form.addEventListener('submit', e => {
    e.preventDefault()
    if ((form.shortener.value).trim() === '') {
        form.shortener.classList.add('error')
        message.textContent = 'Please add a link'


    } else {
        form.shortener.classList.remove('error')
        message.textContent = ''
        const response = postToAPI((form.shortener.value).trim())
        response.then(data => {
                console.log(data)
                const shortener = new Output(data)
                shortener.insertHTML()
        }).catch(e => {
            console.log(e)
        })
        form.reset()


    }
})

middle_cont.addEventListener('click', e => {
    if (e.target.tagName === 'BUTTON' && e.target.classList.contains('copy_btn')) {
        const copy_text = e.target.parentElement.previousElementSibling.lastElementChild
        copyToClipboard(copy_text)
    }
})