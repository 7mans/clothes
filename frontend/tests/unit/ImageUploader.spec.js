/**
 * @description ImageUploader 组件的单元测试
 */

import { shallowMount } from '@vue/test-utils';
import ImageUploader from '@/components/ImageUploader.vue';

// Mock the store
const mockStore = {
  state: {
    auth: {
      token: 'fake-token'
    }
  }
};

// Mock the component
const mountComponent = () => {
  return shallowMount(ImageUploader, {
    mocks: {
      $store: mockStore
    }
  });
};

describe('ImageUploader.vue', () => {
  it('renders upload placeholder text when no image is selected', () => {
    const wrapper = mountComponent();
    const textElement = wrapper.find('.el-upload__text');
    expect(textElement.exists()).toBe(true);
    expect(textElement.text()).toContain('将图片拖到此处，或<em>点击上传</em>');
  });

  it('shows loading state when beforeUpload is called', async () => {
    const wrapper = mountComponent();
    const file = new File(['dummy content'], 'example.png', { type: 'image/png' });
    
    // Call the method
    wrapper.vm.beforeUpload(file);
    await wrapper.vm.$nextTick(); // Wait for DOM update

    expect(wrapper.vm.loading).toBe(true);
    const loadingElement = wrapper.find('.upload-loading');
    expect(loadingElement.exists()).toBe(true);
  });
});
