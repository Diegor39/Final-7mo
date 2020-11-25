import azure.cognitiveservices.speech as sSDK

speech_key, service_region = "e21c5662cc5c4e7aa983ba12c67f6a90", "eastus"
speech_config = sSDK.SpeechConfig(subscription=speech_key, region=service_region)

speech_recognizer = sSDK.SpeechRecognizer(speech_config=speech_config)
print("Say something...")

result = speech_recognizer.recognize_once()

if result.reason == sSDK.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))

<center style="position: absolute; max-width: 700px;display: block; left: calc(50% - 200px)">
                    <div class="card mb-3" >
                        <div class="row no-gutters">
                          <div class="col-md-4">
                            <img src="static/inicio.svg" class="card-img" alt="...">
                          </div>
                          <div class="col-md-8">
                            <div class="card-body">
                              <h5 class="card-title">Onboarding</h5>
                              <div id="carouselExampleCaptions" class="carousel slide" data-ride="carousel">
                                <ol class="carousel-indicators">
                                  <li data-target="#carouselExampleCaptions" data-slide-to="0" class="active"></li>
                                  <li data-target="#carouselExampleCaptions" data-slide-to="1"></li>
                                  <li data-target="#carouselExampleCaptions" data-slide-to="2"></li>
                                </ol>
                                <div class="carousel-inner">
                                  <div class="carousel-item active">
                                    <img src="https://www.xtrafondos.com/wallpapers/cubos-3d-neon-3313.jpg" class="d-block w-100" alt="...">
                                    <div class="carousel-caption d-none d-md-block">
                                      <h5>Ingresa a "Devoluciones y Reembolsos" para ver tus tickets</h5>
                                      <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
                                    </div>
                                  </div>
                                  <div class="carousel-item">
                                    <img src="static/Captura de Pantalla 2020-11-14 a la(s) 22.11.31.png" class="d-block w-100" alt="...">
                                    <div class="carousel-caption d-none d-md-block">
                                      <h5>Second slide label</h5>
                                      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                                    </div>
                                  </div>
                                  <div class="carousel-item">
                                    <img src="..." class="d-block w-100" alt="...">
                                    <div class="carousel-caption d-none d-md-block">
                                      <h5>Third slide label</h5>
                                      <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
                                    </div>
                                  </div>
                                </div>
                                <a class="carousel-control-prev" href="#carouselExampleCaptions" role="button" data-slide="prev">
                                  <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                  <span class="sr-only">Previous</span>
                                </a>
                                <a class="carousel-control-next" href="#carouselExampleCaptions" role="button" data-slide="next">
                                  <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                  <span class="sr-only">Next</span>
                                </a>
                              </div>
                            </div>
                          </div>
                        </div>
                    </div>    
                </center> 