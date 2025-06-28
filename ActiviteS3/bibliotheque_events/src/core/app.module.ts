import { Module } from '@nestjs/common';
import { EventsModule } from '../events/events.module';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { CommonModule } from './common.module';

@Module({
  imports: [EventsModule, CommonModule],
  controllers: [AppController],
  providers: [AppService],
  exports: [],
})
export class AppModule {}
