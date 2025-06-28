import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getWelcomTexts(): { title: string; description: string } {
    return {
      title: "Bienvenue sur l'API des Evenements",
      description: 'Inscrivez des personnes à des évènements.',
    };
  }
}
