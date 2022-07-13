// use absolute path to make sure no circular ref of style
// this -> modal-index -> modal-style
import { h, defineComponent, ref } from 'vue';
import NModal from '../../modal/src/Modal';
import { keep } from '../../_utils';
import { NDialog } from './Dialog';
import { dialogProps, dialogPropKeys } from './dialogProps';
export const exposedDialogEnvProps = Object.assign(Object.assign({}, dialogProps), { blockScroll: { type: Boolean, default: true }, closeOnEsc: { type: Boolean, default: true }, autoFocus: {
        type: Boolean,
        default: true
    }, internalStyle: [String, Object], maskClosable: {
        type: Boolean,
        default: true
    }, onPositiveClick: Function, onNegativeClick: Function, onClose: Function, onMaskClick: Function });
export const NDialogEnvironment = defineComponent({
    name: 'DialogEnvironment',
    props: Object.assign(Object.assign({}, exposedDialogEnvProps), { internalKey: {
            type: String,
            required: true
        }, to: [String, Object], 
        // private
        onInternalAfterLeave: {
            type: Function,
            required: true
        } }),
    setup(props) {
        const showRef = ref(true);
        function handleAfterLeave() {
            props.onInternalAfterLeave(props.internalKey);
        }
        function handlePositiveClick(e) {
            const { onPositiveClick } = props;
            if (onPositiveClick) {
                void Promise.resolve(onPositiveClick(e)).then((result) => {
                    if (result === false)
                        return;
                    hide();
                });
            }
            else {
                hide();
            }
        }
        function handleNegativeClick(e) {
            const { onNegativeClick } = props;
            if (onNegativeClick) {
                void Promise.resolve(onNegativeClick(e)).then((result) => {
                    if (result === false)
                        return;
                    hide();
                });
            }
            else {
                hide();
            }
        }
        function handleCloseClick() {
            const { onClose } = props;
            if (onClose) {
                void Promise.resolve(onClose()).then((result) => {
                    if (result === false)
                        return;
                    hide();
                });
            }
            else {
                hide();
            }
        }
        function handleMaskClick(e) {
            const { onMaskClick, maskClosable } = props;
            if (onMaskClick) {
                onMaskClick(e);
                maskClosable && hide();
            }
        }
        function hide() {
            showRef.value = false;
        }
        function handleUpdateShow(value) {
            showRef.value = value;
        }
        return {
            show: showRef,
            hide,
            handleUpdateShow,
            handleAfterLeave,
            handleCloseClick,
            handleNegativeClick,
            handlePositiveClick,
            handleMaskClick
        };
    },
    render() {
        const { handlePositiveClick, handleUpdateShow, handleNegativeClick, handleCloseClick, handleAfterLeave, handleMaskClick, to, maskClosable, show } = this;
        return (h(NModal, { show: show, onUpdateShow: handleUpdateShow, onMaskClick: handleMaskClick, to: to, maskClosable: maskClosable, onAfterLeave: handleAfterLeave, closeOnEsc: this.closeOnEsc, blockScroll: this.blockScroll, autoFocus: this.autoFocus, internalAppear: true, internalDialog: true }, {
            default: () => (h(NDialog, Object.assign({}, keep(this.$props, dialogPropKeys), { style: this.internalStyle, onClose: handleCloseClick, onNegativeClick: handleNegativeClick, onPositiveClick: handlePositiveClick })))
        }));
    }
});
