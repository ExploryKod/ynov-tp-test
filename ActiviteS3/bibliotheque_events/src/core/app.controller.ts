import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get('/')
  getHomePage() {
    return {
      title: this.appService.getWelcomTexts().title,
      description: this.appService.getWelcomTexts().description,
    };
  }
}
