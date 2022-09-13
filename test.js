import {LibreLinkUpClient} from '@diakem/libre-link-up-api-client';

const {readRaw} = LibreLinkUpClient({username: 'xxx', password: 'xxx'});

const response = await readRaw();