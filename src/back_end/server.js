// Require the framework and instantiate it
const fastify = require('fastify')({ logger: true })
const fs = require('fs')

let currentStatus = ''
let currentMovement = ''
let handleTime = 0

// Declare routes

// Controlling page routes
fastify.get('/normal', async (request, reply) => {
  currentStatus = 'normal'
  return 'normal'
})

fastify.get('/laugh', async (request, reply) => {
  currentStatus = 'laugh'
  return 'laugh'
})

fastify.get('/upset', async (request, reply) => {
  currentStatus = 'upset'
  return 'upset'
})

fastify.get('/surprise', async (request, reply) => {
  currentStatus = 'surprise'
  return 'surprise'
})

fastify.get('/autoFace', async (request, reply) => {
  currentMovement = 'autoFace'
  if(handleTime != 0){
	  clearTimeout(handleTime)
	  handleTime = 0
  }
  handleTime = setTimeout(() => { currentMovement = '' }, 1000) 
  return 'autoFace'
})

fastify.get('/shy', async (request, reply) => {
  currentStatus = 'shy'
  return 'shy'
})

fastify.get('/neckTop', async (request, reply) => {
  currentMovement = 'neckTop'
  if(handleTime != 0){
	  clearTimeout(handleTime)
	  handleTime = 0
  }
  handleTime = setTimeout(() => { currentMovement = '' }, 1000) 
  return 'neckTop'
})

fastify.get('/neckBottom', async (request, reply) => {
  currentMovement = 'neckBottom'
  if(handleTime != 0){
	  clearTimeout(handleTime)
	  handleTime = 0
  }
  handleTime = setTimeout(() => { currentMovement = '' }, 1000) 
  return 'neckBottom'
})

fastify.get('/neckLeft', async (request, reply) => {
  currentMovement = 'neckLeft'
  if(handleTime != 0){
	  clearTimeout(handleTime)
	  handleTime = 0
  }
  handleTime = setTimeout(() => { currentMovement = '' }, 1000) 
  return 'neckLeft'
})

fastify.get('/neckRight', async (request, reply) => {
  currentMovement = 'neckRight'
  if(handleTime != 0){
	  clearTimeout(handleTime)
	  handleTime = 0
  }
  handleTime = setTimeout(() => { currentMovement = '' }, 1000) 
  return 'neckRight'
})

fastify.get('/armLeftTop', async (request, reply) => {
  currentMovement = 'armLeftTop'
  if(handleTime != 0){
	  clearTimeout(handleTime)
	  handleTime = 0
  }
  handleTime = setTimeout(() => { currentMovement = '' }, 1000) 
  return 'armLeftTop'
})

fastify.get('/roundRight', async (request, reply) => {
  currentMovement = 'roundRight'
  if(handleTime != 0){
	  clearTimeout(handleTime)
	  handleTime = 0
  }
  handleTime = setTimeout(() => { currentMovement = '' }, 1000) 
  return 'roundRight'
})

fastify.get('/armLeftBottom', async (request, reply) => {
  currentMovement = 'armLeftBottom'
  if(handleTime != 0){
	  clearTimeout(handleTime)
	  handleTime = 0
  }
  handleTime = setTimeout(() => { currentMovement = '' }, 1000) 
  return 'armLeftBottom'
})

fastify.get('/armRightTop', async (request, reply) => {
  currentMovement = 'armRightTop'
  if(handleTime != 0){
	  clearTimeout(handleTime)
	  handleTime = 0
  }
  handleTime = setTimeout(() => { currentMovement = '' }, 1000) 
  return 'armRightTop'
})

fastify.get('/roundLeft', async (request, reply) => {
  currentMovement = 'roundLeft'
  if(handleTime != 0){
	  clearTimeout(handleTime)
	  handleTime = 0
  }
  handleTime = setTimeout(() => { currentMovement = '' }, 1000) 
  return 'roundLeft'
})

fastify.get('/armRightBottom', async (request, reply) => {
  currentMovement = 'armRightBottom'
  if(handleTime != 0){
	  clearTimeout(handleTime)
	  handleTime = 0
  }
  handleTime = setTimeout(() => { currentMovement = '' }, 1000) 
  return 'armRightBottom'
})

fastify.get('/moveFront', async (request, reply) => {
  currentMovement = 'moveFront'
  if(handleTime != 0){
	  clearTimeout(handleTime)
	  handleTime = 0
  }
  handleTime = setTimeout(() => { currentMovement = '' }, 1000) 
  return 'moveFront'
})

fastify.get('/moveBack', async (request, reply) => {
  currentMovement = 'moveBack'
  if(handleTime != 0){
	  clearTimeout(handleTime)
	  handleTime = 0
  }
  handleTime = setTimeout(() => { currentMovement = '' }, 1000) 
  return 'moveBack'
})

fastify.get('/moveRight', async (request, reply) => {
  currentMovement = 'moveRight'
  if(handleTime != 0){
	  clearTimeout(handleTime)
	  handleTime = 0
  }
  handleTime = setTimeout(() => { currentMovement = '' }, 1000) 
  return 'moveRight'
})

fastify.get('/moveLeft', async (request, reply) => {
  currentMovement = 'moveLeft'
  if(handleTime != 0){
	  clearTimeout(handleTime)
	  handleTime = 0
  }
  handleTime = setTimeout(() => { currentMovement = '' }, 1000) 
  return 'moveLeft'
})



// Client routes


fastify.get('/checkMovement', async (request, reply) => {
  return currentMovement
})

// Run the server!
const start = async () => {
  try {
    await fastify.listen(3000,'127.0.0.1')
  } catch (err) {
    fastify.log.error(err)
    process.exit(1)
  }
}
start()
