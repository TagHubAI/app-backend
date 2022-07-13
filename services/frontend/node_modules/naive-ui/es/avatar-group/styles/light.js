import { commonLight } from '../../_styles/common';
import { createTheme } from '../../_mixins';
import { avatarLight } from '../../avatar/styles';
const avatarGroupLight = createTheme({
    name: 'AvatarGroup',
    common: commonLight,
    peers: {
        Avatar: avatarLight
    }
});
export default avatarGroupLight;
