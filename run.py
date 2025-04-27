from todor import create_app

if __name__ =='__main__':
    app = create_app()
    # host="0.0.0.0" hace que escuche fuera del contenedor
    app.run(host="0.0.0.0", port=5000, debug=True)
    
    
    #app.run()