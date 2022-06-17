export default [
  {
    _name: 'CSidebarNav',
    _children: [
      {
        _name: 'CSidebarNavItem',
        name: 'Главная',
        to: '/dashboard',
        icon: 'cil-speedometer',
        badge: {
          color: 'primary',
          text: 'NEW'
        }
      },
      {
        _name: 'CSidebarNavItem',
        name: 'Рейтинг школ',
        to: '/rating',
        
      },
      {
        _name: 'CSidebarNavDropdown',
        name: 'Курсы',
        route: '/courses',
        icon: 'cil-puzzle',
        items: [
          {
            name: 'Все классы',
            to: '/courses'
          },
          {
            name: '6 класс',
            to: '/courses/6'
          },
        ]
      },
      {
        _name: 'CSidebarNavItem',
        name: 'Графики(debug)',
        to: '/charts',
        icon: 'cil-chart-pie'
      },
      {
        _name: 'CSidebarNavTitle',
        _children: ['Аккаунт']
      },
      {
        _name: 'CSidebarNavItem',
        name: 'Войти',
        to: '/pages/login',
        icon: 'cil-user'
      },
      {
        _name: 'CSidebarNavItem',
        name: 'Регистрация',
        to: '/pages/register',
        icon: 'cil-user-follow'
      }
    ]
  }
]