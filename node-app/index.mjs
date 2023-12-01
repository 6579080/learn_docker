import fs from 'fs'

fs.appendFile('my-file.txt', 'файл создан node.js', (err)=>{
    if (err) throw err
    console.log('файл сохранен')
})


setTimeout(()=> console.log('конец'), 30000)