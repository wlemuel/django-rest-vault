const Salsa20 = require('node-salsa20')
const { Base64 } = require('js-base64')
const randomBytes = require('random-bytes')

const key = '*Thirty-two byte (256 bits) key*'

const stringToUint8Array = (str) => {
  let encoder = new TextEncoder()
  return encoder.encode(str)
}

const uint8ArrayToString = (bytes) => {
  let decoder = new TextDecoder()
  return decoder.decode(bytes)
}

// const encryptor1 = new Salsa20({ doubleRounds: 10 }).key(stringToUint8Array(key));
// const encryptor2 = new Salsa20({ rounds: 20 }).key(stringToUint8Array(key));

function encrypt_data(data) {
  let encryptor2 = new Salsa20({ rounds: 20 }).key(stringToUint8Array(key))
  let nonce = new Uint8Array(randomBytes.sync(8))
  let cipher = encryptor2.nonce(nonce)
  let encrypted_data = new Uint8Array(cipher.encrypt(stringToUint8Array(data)))
  encrypt_data = new Uint8Array([...nonce, ...encrypted_data])
  let b64_data = Base64.fromUint8Array(encrypt_data)

  return b64_data
}

function decrypt_data(data) {
  let encryptor2 = new Salsa20({ rounds: 20 }).key(stringToUint8Array(key))
  let decoded_msg = Base64.toUint8Array(data)
  let nonce = decoded_msg.slice(0, 8)
  let msg = decoded_msg.slice(8)

  let cipher = encryptor2.nonce(nonce)

  let result = cipher.decrypt(msg)

  return uint8ArrayToString(result)
}

function main() {
  let message =
    'zIkyqayXbGvP7/+nWqjaz8BRTGWcpmaNa8qZGA87BQrNk2FWXX5sHdBC7neqabPNeZyysUOuhMsm'
  let raw_message = '[{"a": 1, "b": 2, "c": "中文", "d": 4, "e": 5}]'

  console.log(encrypt_data(raw_message))
  console.log(decrypt_data(message))
}

main()
